import falcon


class SLComputeV2OSSecurityGroups(object):
    def on_get(self, req, resp, tenant_id, instance_id=None):
        resp.status = falcon.HTTP_200
        resp.body = {
            'security_groups': [{
                'description': 'default',
                'id': 1,
                'name': 'default',
                'rules': {},
                'tenant_id': tenant_id,
            }]}