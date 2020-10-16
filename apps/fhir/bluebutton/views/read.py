import logging
from rest_framework import permissions

from apps.authorization.permissions import DataAccessGrantPermission
from apps.capabilities.permissions import TokenHasProtectedCapability
from ..permissions import (ReadCrosswalkPermission, ResourcePermission, ApplicationActivePermission)
from apps.fhir.bluebutton.views.generic import FhirDataView

logger = logging.getLogger('hhs_server.%s' % __name__)


#####################################################################
# These functions are a stepping stone to a single class based view #
#####################################################################

class ReadView(FhirDataView):
    # BB2-149 note, check authenticated first, then app active etc.
    permission_classes = [
        permissions.IsAuthenticated,
        ApplicationActivePermission,
        ResourcePermission,
        ReadCrosswalkPermission,
        DataAccessGrantPermission,
        TokenHasProtectedCapability,
    ]

    def build_parameters(self, *args, **kwargs):
        return {
            "_format": "json"
        }

    def build_url(self, resource_router, resource_type, resource_id, **kwargs):
        return resource_router.fhir_url + resource_type + "/" + resource_id + "/"
