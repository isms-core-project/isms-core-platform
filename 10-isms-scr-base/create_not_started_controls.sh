#!/bin/bash

# Create control folders for Not Started (POL = ⭕) controls

# Array of control folder names
controls=(
    # SECTION 5: ORGANIZATIONAL CONTROLS
    "ISMS-A.5.3-Segregation-of-Duties"
    "ISMS-A.5.8-Information-Security-in-Project-Management"
    "ISMS-A.5.12-13-Classification-and-Labelling"
    "ISMS-A.5.14-Information-Transfer"
    "ISMS-A.5.17-Authentication-Information"
    "ISMS-A.5.24-28-Incident-Management-Lifecycle"
    "ISMS-A.5.33-Protection-of-Records"
    "ISMS-A.5.34-Privacy-and-PII"
    "ISMS-A.5.36-Compliance-Checking"
    
    # SECTION 6: PEOPLE CONTROLS
    "ISMS-A.6.3-Awareness-and-Training"
    "ISMS-A.6.7-8-Remote-Working-and-Reporting"
    
    # SECTION 7: PHYSICAL CONTROLS
    "ISMS-A.7.1-2-3-Physical-Access-Control"
    "ISMS-A.7.6-7-14-Information-Media-Handling"
    "ISMS-A.7.8-9-Equipment-Location-Security"
    "ISMS-A.7.10-Delivery-and-Loading-Areas"
    "ISMS-A.7.12-13-Infrastructure-Maintenance"
)

# Create each control folder
for control in "${controls[@]}"; do
    if [ ! -d "$control" ]; then
        mkdir -p "$control"
        echo "✅ Created: $control"
    else
        echo "⚠️  Already exists: $control"
    fi
done

echo ""
echo "📊 Summary: ${#controls[@]} control folders processed"