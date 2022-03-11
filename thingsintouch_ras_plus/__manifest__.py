# Copyright (C) 2018 Creu Blanca
# Copyright (C) 2021 thingsintouch.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "'RAS plus' Configuration for IoT/OCA",
    "version": "13.0.1.0.0",
    "category": "IoT",
    "author": "Creu Blanca , "
            "thingsintouch.com",
    "website": "https://github.com/thingsintouch/iot-devices",
    "license": "AGPL-3",
    "installable": True,
    "summary": "Template and Functionality to define new 'RAS plus' Devices (RAS with relay) for OCA-IoT Modules",
    "depends": ["thingsintouch_ras_attendance", "iot_rule", "iot_key_employee_rfid"],
    "data": ["data/ras_plus_template.xml"],
}
