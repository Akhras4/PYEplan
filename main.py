import xml.etree.ElementTree as ET


# Load and parse the XML file
tree = ET.parse('PYEplan/ProjectInfo.xml')  
root = tree.getroot()

# Function to find property value by name (or partial name)
def find_property_value(name):
    for prop in root.findall('Property'):
        prop_name = prop.attrib.get('name', '')
        if name.lower() in prop_name.lower():
            # Try extracting from 'value' attribute if 'text' is missing
            return prop.attrib.get('value', prop.text)
    return None

# Extract project information dynamically
project_info = {
    "project_name": find_property_value("Project name (full)"),
    "job_number": find_property_value("Job number"),
    "project_path": find_property_value("Project path (full)"),
    "company_details": {
        "name": find_property_value("Company name"),
        "address": f"{find_property_value('Company address 1') or ''}, {find_property_value('Company address 2') or ''}".strip(", "),
        "phone": find_property_value("Creator: Phone")
    },
    "creation_details": {
        "creator": find_property_value("Creator"),
        "last_editor": find_property_value("Last editor: Sign-in name"),
        "creation_date": find_property_value("Creation date"),
        "last_modification_date": find_property_value("Modification date"),
        "last_eplan_version": find_property_value("Last EPLAN version used"),
        "build_number": find_property_value("Last EPLAN build number used")
    },
    "additional_info": {
        "total_pages": find_property_value("Total no. of pages"),
        "created_pages": find_property_value("Created pages"),
        "report_pages": find_property_value("Generated report pages"),
        "eplan_license_number": find_property_value("License number of dongle"),
        "manufacturing_date": find_property_value("Manufacturing date"),
        "source_language": find_property_value("Source language")
    }
}

# Print the extracted project information
print("\n📂 Extracted Project Information:")
for section, details in project_info.items():
    if isinstance(details, dict):
        print(f"\n🔹 {section.replace('_', ' ').title()}:")
        for key, value in details.items():
            print(f"   ➜ {key.replace('_', ' ').title()}: {value}")
    else:
        print(f"{section.replace('_', ' ').title()}: {details}")
