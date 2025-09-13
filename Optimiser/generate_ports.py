# updated_port_data_generator.py
import json

# --- 1. Define Country Code Mapping ---
# Using standard 2-letter ISO country codes.
# Add/modify based on the countries present in your ports.json
COUNTRY_CODES = {
    # Official ISO Codes
    "Andorra": "AD",
    "United Arab Emirates": "AE",
    "Afghanistan": "AF",
    "Antigua and Barbuda": "AG",
    "Anguilla": "AI",
    "Albania": "AL",
    "Armenia": "AM",
    "Angola": "AO",
    "Antarctica": "AQ",
    "Argentina": "AR",
    "American Samoa": "AS",
    "Austria": "AT",
    "Australia": "AU",
    "Aruba": "AW",
    "Åland Islands": "AX",
    "Azerbaijan": "AZ",
    "Bosnia and Herzegovina": "BA",
    "Barbados": "BB",
    "Bangladesh": "BD",
    "Belgium": "BE",
    "Burkina Faso": "BF",
    "Bulgaria": "BG",
    "Bahrain": "BH",
    "Burundi": "BI",
    "Benin": "BJ",
    "Saint Barthélemy": "BL",
    "Bermuda": "BM",
    "Brunei Darussalam": "BN",
    "Bolivia, Plurinational State of": "BO",
    "Bonaire, Sint Eustatius and Saba": "BQ",
    "Brazil": "BR",
    "Bahamas": "BS",
    "Bhutan": "BT",
    "Bouvet Island": "BV",
    "Botswana": "BW",
    "Belarus": "BY",
    "Belize": "BZ",
    "Canada": "CA",
    "Cocos (Keeling) Islands": "CC",
    "Congo, Democratic Republic of the": "CD",
    "Central African Republic": "CF",
    "Congo": "CG",
    "Switzerland": "CH",
    "Côte d'Ivoire": "CI",
    "Cook Islands": "CK",
    "Chile": "CL",
    "Cameroon": "CM",
    "China": "CN",
    "Colombia": "CO",
    "Costa Rica": "CR",
    "Cuba": "CU",
    "Cabo Verde": "CV",
    "Curaçao": "CW",
    "Christmas Island": "CX",
    "Cyprus": "CY",
    "Czechia": "CZ",
    "Germany": "DE",
    "Djibouti": "DJ",
    "Denmark": "DK",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Algeria": "DZ",
    "Ecuador": "EC",
    "Estonia": "EE",
    "Egypt": "EG",
    "Western Sahara": "EH",
    "Eritrea": "ER",
    "Spain": "ES",
    "Ethiopia": "ET",
    "Finland": "FI",
    "Fiji": "FJ",
    "Falkland Islands (Malvinas)": "FK",
    "Micronesia, Federated States of": "FM",
    "Faroe Islands": "FO",
    "France": "FR",
    "Gabon": "GA",
    "United Kingdom of Great Britain and Northern Ireland": "GB",
    "Grenada": "GD",
    "Georgia": "GE",
    "French Guiana": "GF",
    "Guernsey": "GG",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greenland": "GL",
    "Gambia": "GM",
    "Guinea": "GN",
    "Guadeloupe": "GP",
    "Equatorial Guinea": "GQ",
    "Greece": "GR",
    "South Georgia and the South Sandwich Islands": "GS",
    "Guatemala": "GT",
    "Guam": "GU",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Hong Kong": "HK",
    "Heard Island and McDonald Islands": "HM",
    "Honduras": "HN",
    "Croatia": "HR",
    "Haiti": "HT",
    "Hungary": "HU",
    "Indonesia": "ID",
    "Ireland": "IE",
    "Israel": "IL",
    "Isle of Man": "IM",
    "India": "IN",
    "British Indian Ocean Territory": "IO",
    "Iraq": "IQ",
    "Iran, Islamic Republic of": "IR",
    "Iceland": "IS",
    "Italy": "IT",
    "Jersey": "JE",
    "Jamaica": "JM",
    "Jordan": "JO",
    "Japan": "JP",
    "Kenya": "KE",
    "Kyrgyzstan": "KG",
    "Cambodia": "KH",
    "Kiribati": "KI",
    "Comoros": "KM",
    "Saint Kitts and Nevis": "KN",
    "Korea, Democratic People's Republic of": "KP",
    "Korea, Republic of": "KR",
    "Kuwait": "KW",
    "Cayman Islands": "KY",
    "Kazakhstan": "KZ",
    "Lao People's Democratic Republic": "LA",
    "Lebanon": "LB",
    "Saint Lucia": "LC",
    "Liechtenstein": "LI",
    "Sri Lanka": "LK",
    "Liberia": "LR",
    "Lesotho": "LS",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Latvia": "LV",
    "Libya": "LY",
    "Morocco": "MA",
    "Monaco": "MC",
    "Moldova, Republic of": "MD",
    "Montenegro": "ME",
    "Saint Martin (French part)": "MF",
    "Madagascar": "MG",
    "Marshall Islands": "MH",
    "North Macedonia": "MK",
    "Mali": "ML",
    "Myanmar": "MM",
    "Mongolia": "MN",
    "Macao": "MO",
    "Northern Mariana Islands": "MP",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Montserrat": "MS",
    "Malta": "MT",
    "Mauritius": "MU",
    "Maldives": "MV",
    "Malawi": "MW",
    "Mexico": "MX",
    "Malaysia": "MY",
    "Mozambique": "MZ",
    "Namibia": "NA",
    "New Caledonia": "NC",
    "Niger": "NE",
    "Norfolk Island": "NF",
    "Nigeria": "NG",
    "Nicaragua": "NI",
    "Netherlands, Kingdom of the": "NL",
    "Norway": "NO",
    "Nepal": "NP",
    "Nauru": "NR",
    "Niue": "NU",
    "New Zealand": "NZ",
    "Oman": "OM",
    "Panama": "PA",
    "Peru": "PE",
    "French Polynesia": "PF",
    "Papua New Guinea": "PG",
    "Philippines": "PH",
    "Pakistan": "PK",
    "Poland": "PL",
    "Saint Pierre and Miquelon": "PM",
    "Pitcairn": "PN",
    "Puerto Rico": "PR",
    "Palestine, State of": "PS",
    "Portugal": "PT",
    "Palau": "PW",
    "Paraguay": "PY",
    "Qatar": "QA",
    "Réunion": "RE",
    "Romania": "RO",
    "Serbia": "RS",
    "Russian Federation": "RU",
    "Rwanda": "RW",
    "Saudi Arabia": "SA",
    "Solomon Islands": "SB",
    "Seychelles": "SC",
    "Sudan": "SD",
    "Sweden": "SE",
    "Singapore": "SG",
    "Saint Helena, Ascension and Tristan da Cunha": "SH",
    "Slovenia": "SI",
    "Svalbard and Jan Mayen": "SJ",
    "Slovakia": "SK",
    "Sierra Leone": "SL",
    "San Marino": "SM",
    "Senegal": "SN",
    "Somalia": "SO",
    "Suriname": "SR",
    "South Sudan": "SS",
    "Sao Tome and Principe": "ST",
    "El Salvador": "SV",
    "Sint Maarten (Dutch part)": "SX",
    "Syrian Arab Republic": "SY",
    "Eswatini": "SZ",
    "Turks and Caicos Islands": "TC",
    "Chad": "TD",
    "French Southern Territories": "TF",
    "Togo": "TG",
    "Thailand": "TH",
    "Tajikistan": "TJ",
    "Tokelau": "TK",
    "Timor-Leste": "TL",
    "Turkmenistan": "TM",
    "Tunisia": "TN",
    "Tonga": "TO",
    "Türkiye": "TR", # Updated name
    "Trinidad and Tobago": "TT",
    "Tuvalu": "TV",
    "Taiwan, Province of China": "TW",
    "Tanzania, United Republic of": "TZ",
    "Ukraine": "UA",
    "Uganda": "UG",
    "United States Minor Outlying Islands": "UM",
    "United States of America": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Holy See": "VA",
    "Saint Vincent and the Grenadines": "VC",
    "Venezuela, Bolivarian Republic of": "VE",
    "Virgin Islands (British)": "VG",
    "Virgin Islands (U.S.)": "VI",
    "Viet Nam": "VN",
    "Vanuatu": "VU",
    "Wallis and Futuna": "WF",
    "Samoa": "WS",
    "Yemen": "YE",
    "Mayotte": "YT",
    "South Africa": "ZA",
    "Zambia": "ZM",
    "Zimbabwe": "ZW",
    # Common Aliases (Add as needed based on your data)
    "U.S.A.": "US",
    "U.K.": "GB", # Official code is GB, .uk is the ccTLD
    "Russia": "RU", # Common name vs ISO name Russian Federation
    "Czech Republic": "CZ", # Previous ISO name vs current Czechia
    "Burma": "MM", # Previous name vs current Myanmar
    "Ivory Coast": "CI", # Common name vs ISO name Côte d'Ivoire
    "Swaziland": "SZ", # Previous name vs current Eswatini
    "Macedonia, the former Yugoslav Republic of": "MK", # Previous name vs current North Macedonia
    "Vietnam": "VN", # Common name vs ISO name Viet Nam
    # Add more aliases if your ports.json uses them
}

# --- 2. Load data from ports.json ---
try:
    with open('ports.json', 'r', encoding='utf-8') as f:
        raw_locations = json.load(f)
    print(f"Successfully loaded {len(raw_locations)} locations from ports.json")
except FileNotFoundError:
    print("Error: 'ports.json' file not found in the current directory.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON format in 'ports.json': {e}")
    exit(1)

# --- 3. Process Data and Generate New Dictionary (Initial Step) ---
def generate_initial_port_data(raw_locations, country_codes):
    """
    Generates a new list of port data dictionaries from the raw location data,
    assigning new unique codes.
    """
    generated_port_data = []
    country_counters = {} # To keep track of the incrementing number per country

    for location in raw_locations:
        city = location.get("CITY", "Unknown City").strip()
        # Normalize country name for lookup (strip periods, potentially map aliases)
        raw_country = location.get("COUNTRY", "Unknown Country").rstrip('.').strip()
        state = location.get("STATE", "").strip()
        try:
            lat = float(location.get("LATITUDE", 0.0))
            lng = float(location.get("LONGITUDE", 0.0))
        except (ValueError, TypeError):
            print(f"Warning: Invalid latitude/longitude for {city}, {raw_country}. Skipping.")
            continue

        # Get standardized country code
        country_code = country_codes.get(raw_country)
        if not country_code:
            print(f"Warning: Country code not found for '{raw_country}'. Assigning 'XX'.")
            country_code = "XX" # Default code for unknown countries

        # Increment and get the city counter for this country
        if country_code not in country_counters:
            country_counters[country_code] = 1
        else:
            country_counters[country_code] += 1
        city_counter = country_counters[country_code]

        # Create the unique port code (e.g., US0001, US0002, CN0001)
        # Pad the counter with zeros to make it 4 digits (adjust padding as needed)
        padded_counter = str(city_counter).zfill(4)
        unique_code = f"{country_code}{padded_counter}"

        # Create the entry
        info_text = f"{city}"
        if state:
             info_text += f", {state}"
        info_text += f", {raw_country}"

        port_entry = {
            "name": city,
            "country": raw_country,
            "lat": lat,
            "lng": lng,
            "code": unique_code, # Newly generated code
            "info": info_text # Basic info
        }

        generated_port_data.append(port_entry)

    return generated_port_data

# --- 4. Add 'is_accepted' Flag, Remove Duplicates ---
def add_accepted_flag_and_deduplicate(initial_port_data):
    """
    Reads accepted_ports.json, adds 'is_accepted' flag to the initial port data,
    and removes duplicate ports based on the 'name' field.
    """
    # --- Load Accepted Ports ---
    accepted_ports_filename = "accepted_ports.json"
    try:
        with open(accepted_ports_filename, 'r', encoding='utf-8') as f:
            accepted_ports_data = json.load(f)
        print(f"\nSuccessfully loaded {len(accepted_ports_data)} accepted ports from '{accepted_ports_filename}'")
    except FileNotFoundError:
        print(f"Warning: File '{accepted_ports_filename}' not found. 'is_accepted' will be False for all ports.")
        accepted_ports_data = [] # Treat as empty list
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{accepted_ports_filename}': {e}. 'is_accepted' will be False for all ports.")
        accepted_ports_data = [] # Treat as empty list
    except Exception as e:
        print(f"Error loading '{accepted_ports_filename}': {e}. 'is_accepted' will be False for all ports.")
        accepted_ports_data = [] # Treat as empty list

    # Create a set of accepted city names for fast lookup (case-insensitive)
    accepted_cities_set = {port["CITY"].lower().strip() for port in accepted_ports_data}
    print(f"Created lookup set for {len(accepted_cities_set)} unique accepted city names.")

    # --- Deduplicate and Add 'is_accepted' Flag ---
    seen_names = set()
    final_port_data = []
    duplicate_count = 0
    updated_port_count = 0

    for port in initial_port_data:
        port_name = port.get("name", "")
        port_name_lower = port_name.lower().strip()

        # Check for duplicates
        if port_name_lower in seen_names:
            duplicate_count += 1
            # print(f"Skipping duplicate port: {port_name}") # Optional: log skipped duplicates
            continue # Skip adding this port

        # If not a duplicate, process it
        seen_names.add(port_name_lower)
        # Determine if the port name is in the accepted cities list
        is_accepted = port_name_lower in accepted_cities_set
        # Add the flag to the port dictionary
        port["is_accepted"] = is_accepted
        final_port_data.append(port)
        updated_port_count += 1

    print(f"Removed {duplicate_count} duplicate ports.")
    print(f"Processed {updated_port_count} unique ports and added 'is_accepted' flag.")

    return final_port_data

# --- 5. Save the Final Data ---
def save_final_port_data(final_port_data):
    """
    Saves the final port data (with is_accepted flags, duplicates removed)
    to JSON and JS files.
    """
    # --- Save to JSON ---
    json_output_filename = "generated_port_data_from_json.json"
    try:
        with open(json_output_filename, 'w', encoding='utf-8') as f:
            json.dump(final_port_data, f, indent=4)
        print(f"\nFinal port data (with flags, deduplicated) saved to '{json_output_filename}'")
    except Exception as e:
        print(f"Error saving final data to JSON file: {e}")
        return False # Indicate failure

    # --- Save to JavaScript ---
    js_output_filename = "generated_port_data_from_json.js"
    try:
        with open(js_output_filename, 'w', encoding='utf-8') as f:
            f.write("// Generated Port Data (Updated with is_accepted flags and duplicates removed)\n")
            # Using 'var' for broader compatibility if needed, or 'const'
            f.write("var generatedPortDataFromJson = ")
            json.dump(final_port_data, f, indent=4) # Write the list directly
            f.write(";\n")
        print(f"Final port data also saved as JS variable to '{js_output_filename}'")
        print("You can include this in your HTML with: <script src='generated_port_data_from_json.js'></script>")
    except Exception as e:
        print(f"Error saving final data to JS file: {e}")
        return False # Indicate failure

    print(f"\nTotal final entries: {len(final_port_data)}")
    return True # Indicate success

# --- Main Execution Flow ---
if __name__ == "__main__":
    # Step 1: Generate initial port data
    print("--- Generating initial port data ---")
    initial_port_data_list = generate_initial_port_data(raw_locations, COUNTRY_CODES)

    # Print first few for verification of initial step
    print("\nFirst 5 generated entries (initial):")
    for entry in initial_port_data_list[:5]:
        print(entry)

    print(f"\nTotal initial entries generated: {len(initial_port_data_list)}")

    # Step 2: Add flags, remove duplicates
    print("\n--- Adding 'is_accepted' flag and removing duplicates ---")
    final_port_data_list = add_accepted_flag_and_deduplicate(initial_port_data_list)

    # Step 3: Save the final data
    print("\n--- Saving final port data ---")
    success = save_final_port_data(final_port_data_list)

    if success:
        print("\n--- Process completed successfully! ---")
        print("Use the newly generated 'generated_port_data_from_json.json' and 'generated_port_data_from_json.js' files in your project.")
    else:
        print("\n--- Process failed during saving step. ---")
