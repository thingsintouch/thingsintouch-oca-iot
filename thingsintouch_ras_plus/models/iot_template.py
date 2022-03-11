# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging

from odoo import models
from odoo import _

_logger = logging.getLogger(__name__)


class IotTemplate(models.Model):
    _inherit = "iot.template"

    def _get_keys(self, serial):
        result = super()._get_keys(serial)
        if self == self.env.ref("thingsintouch_ras_plus.ras_plus_template"):
            lock_1 = self.env["iot.lock"].create({"name": result.get("lock_id_1")})
            result["lock_id_1"] = lock_1.id
        return result
