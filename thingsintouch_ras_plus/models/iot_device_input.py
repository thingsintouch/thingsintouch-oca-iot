# Copyright 2021 thingsintouch.com
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models

from datetime import datetime

import freezegun

class IotDeviceInput(models.Model):
    _inherit = "iot.device.input"


    def call_lock(self, value, state = ""):
        result = super().call_lock(value)
        last_created_action_id = self.env["iot.key.action"].search([], limit=1, order='id desc')[0]
        if result["access_granted"]:
            last_created_action_id["result"] = state or "accepted"
        else:
            last_created_action_id["result"] = "refused"
        return result, last_created_action_id

    @api.model
    def call_lock_async(self, value, timestamp, state):
        with freezegun.freeze_time(datetime.fromtimestamp(int(timestamp), tz=None)):
            result, last_created_action_id = self.call_lock(value, state)
        if not result["access_granted"]:
            last_created_action_id["result"] = state + "- unauthorized key: " + value # this should NEVER happen
        return result
