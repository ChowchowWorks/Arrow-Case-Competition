# calculate_routes_for_accepted_ports.py
import json
import re # Import the 're' module for regular expressions
from searoute import searoute  # Import the searoute function

# --- Function to calculate a single sea route ---
def get_sea_route_points(origin_lon, origin_lat, destination_lon, destination_lat):
    """
    Calculates the sea route points using searoute-py.
    Args:
        origin_lon (float): Longitude of the starting point.
        origin_lat (float): Latitude of the starting point.
        destination_lon (float): Longitude of the destination point.
        destination_lat (float): Latitude of the destination point.
    Returns:
        list[list[float]]: A list of [longitude, latitude] points representing the route,
                           or None if calculation fails.
    """
    try:
        # Define origin and destination as [lon, lat]
        origin = [origin_lon, origin_lat]
        destination = [destination_lon, destination_lat]

        # Calculate the shortest sea route using searoute
        route = searoute(origin, destination)

        # Extract coordinates from the route (GeoJSON format)
        route_coordinates = route['geometry']['coordinates']

        # Ensure the route has valid points
        if route_coordinates and len(route_coordinates) > 1:
            return route_coordinates
        else:
            print(f"  Warning: No valid route found between {origin} and {destination}")
            return None

    except Exception as e:
        print(f"  Error calculating route with searoute between ({origin_lon}, {origin_lat}) and ({destination_lon}, {destination_lat}): {e}")
        return None

# --- Main Script Logic ---
def main():
    # --- 1. Load the generated port data from the JS file ---
    # This file contains the JavaScript variable definition
    input_js_filename = "generated_port_data_from_json.js"
    try:
        with open(input_js_filename, 'r', encoding='utf-8') as f:
            js_content = f.read()
        print(f"Successfully read content from '{input_js_filename}'")
    except FileNotFoundError:
        print(f"Error: Input JS file '{input_js_filename}' not found.")
        return
    except Exception as e:
        print(f"Error reading '{input_js_filename}': {e}")
        return

    # --- 2. Extract JSON data from the JS content ---
    # Use regular expression to find the part after the assignment operator '=' and before the final ';'
    # This assumes the format is like: var generatedPortDataFromJson = [...];
    # The regex looks for 'var generatedPortDataFromJson =' (or 'const ... =' etc.) followed by
    # everything (non-greedy) until the first semicolon.
    match = re.search(r'generatedPortDataFromJson\s*=\s*(.*?);', js_content, re.DOTALL)
    if not match:
        print("Error: Could not find the 'generatedPortDataFromJson' variable assignment in the JS file.")
        return

    json_string = match.group(1)
    # print(f"Extracted JSON string snippet: {json_string[:100]}...") # For debugging

    # --- 3. Parse the extracted JSON string ---
    try:
        GENERATED_PORT_DATA_PYTHON = json.loads(json_string)
        print(f"Successfully parsed JSON data. Total ports: {len(GENERATED_PORT_DATA_PYTHON)}")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse the extracted JSON content: {e}")
        return
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return

    # --- 4. Filter GENERATED_PORT_DATA_PYTHON using the 'is_accepted' flag ---
    # Only include ports explicitly marked as accepted
    FILTERED_PORT_DATA = [
        port for port in GENERATED_PORT_DATA_PYTHON
        if port.get("is_accepted") is True # Check for boolean True
    ]
    print(f"Filtered down to {len(FILTERED_PORT_DATA)} ports that are marked as accepted (is_accepted=true).")

    # --- 5. Calculate Routes ---
    routes_data = {}
    num_ports = len(FILTERED_PORT_DATA)

    if num_ports == 0:
        print("No accepted ports found. No routes to calculate.")
        # Save an empty file
        output_filename = "calculated_sea_routes_for_accepted_ports.json"
        try:
            with open(output_filename, 'w') as f:
                json.dump(routes_data, f, indent=4) # Dump empty dict
            print(f"Saved empty routes data to '{output_filename}'")
        except Exception as e:
            print(f"Error saving empty routes file '{output_filename}': {e}")
        return

    print(f"Calculating routes for {num_ports} accepted ports...")
    # Calculate routes between pairs (A->B, not B->A separately if symmetric)
    calculated_count = 0
    for i, port_a in enumerate(FILTERED_PORT_DATA):
        for port_b in FILTERED_PORT_DATA[i + 1:]:
            route_key = f"{port_a['code']}-{port_b['code']}"
            print(f"Calculating route {calculated_count + 1}/{num_ports * (num_ports - 1) // 2}: {port_a['name']} ({port_a['code']}) -> {port_b['name']} ({port_b['code']})")

            # Get coordinates (Note: searoute expects [lon, lat])
            try:
                origin_coords = (port_a['lng'], port_a['lat'])  # lng, lat
                dest_coords = (port_b['lng'], port_b['lat'])    # lng, lat
            except KeyError as e:
                print(f"  Error: Missing coordinate key {e} for port {port_a['name']} or {port_b['name']}. Skipping.")
                continue

            # Calculate the route using searoute
            route_points = get_sea_route_points(
                origin_coords[0], origin_coords[1],
                dest_coords[0], dest_coords[1]
            )

            if route_points and len(route_points) > 1:
                # Store the route points. Keyed by port codes.
                routes_data[route_key] = route_points
                print(f"  Success: Route has {len(route_points)} points.")
                calculated_count += 1
            else:
                print(f"  Failed: Could not calculate or invalid route.")

    # --- 6. Save the Calculated Routes ---
    output_filename = "calculated_sea_routes_for_accepted_ports.json"
    try:
        with open(output_filename, 'w') as f:
            json.dump(routes_data, f, indent=4)
        print(f"\nRoutes calculation finished. Data saved to '{output_filename}'")
        print(f"Total routes calculated: {len(routes_data)}")
    except Exception as e:
        print(f"Error saving routes to file '{output_filename}': {e}")

if __name__ == "__main__":
    main()
