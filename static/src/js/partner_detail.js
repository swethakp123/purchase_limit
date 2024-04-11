/** @odoo-module */

import { PartnerDetailsEdit } from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { Order } from "@point_of_sale/app/store/models";

patch(PartnerDetailsEdit.prototype, {
    setup() {
        super.setup(...arguments);
        this.intFields.push("purchase_limit");
        this.changes.purchase_limit =
                this.props.partner.purchase_limit;
    }
});

patch(PosStore.prototype,{
    async _processData(loadedData) {
        await super._processData(...arguments);
            this.purchase_limit = loadedData["purchase_limit"];
            },
});