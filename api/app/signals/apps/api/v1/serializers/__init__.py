"""
V1 API Serializers.
"""
from signals.apps.api.v1.serializers.attachment import (
    PrivateSignalAttachmentSerializer,
    PublicSignalAttachmentSerializer,
    SignalAttachmentSerializer
)
from signals.apps.api.v1.serializers.category import (
    CategoryHALSerializer,
    ParentCategoryHALSerializer,
    PrivateCategorySerializer
)
from signals.apps.api.v1.serializers.departments import (
    PrivateDepartmentSerializerDetail,
    PrivateDepartmentSerializerList
)
from signals.apps.api.v1.serializers.question import PublicQuestionSerializerDetail
from signals.apps.api.v1.serializers.signal import (
    AbridgedChildSignalSerializer,
    PrivateSignalSerializerDetail,
    PrivateSignalSerializerList,
    PublicSignalCreateSerializer,
    PublicSignalSerializerDetail,
    SignalGeoSerializer,
    SignalIdListSerializer
)
from signals.apps.api.v1.serializers.signal_history import HistoryHalSerializer
from signals.apps.api.v1.serializers.signal_split import PrivateSplitSignalSerializer
from signals.apps.api.v1.serializers.status_message_template import (
    StateStatusMessageTemplateListSerializer,
    StateStatusMessageTemplateSerializer
)
from signals.apps.api.v1.serializers.stored_signal_filter import StoredSignalFilterSerializer

# new
from signals.apps.api.v1.serializers.country import CountrySerializer
from signals.apps.api.v1.serializers.city import CitySerializer
from signals.apps.api.v1.serializers.city_object import CityObjectSerializer
from signals.apps.api.v1.serializers.signal_city_object import SignalCityObjectSerializerList
from signals.apps.api.v1.serializers.signal_city_object import SignalCityObjectSerializerDetail

__all__ = [
    'PublicSignalAttachmentSerializer',
    'PrivateSignalAttachmentSerializer',
    'SignalAttachmentSerializer',
    'StateStatusMessageTemplateListSerializer',
    'StateStatusMessageTemplateSerializer',
    'CategoryHALSerializer',
    'ParentCategoryHALSerializer',
    'HistoryHalSerializer',
    'PrivateDepartmentSerializerDetail',
    'PrivateDepartmentSerializerList',
    'PrivateSignalSerializerDetail',
    'PrivateSignalSerializerList',
    'PublicSignalSerializerDetail',
    'PublicSignalCreateSerializer',
    'PrivateSplitSignalSerializer',
    'SignalGeoSerializer',
    'SignalIdListSerializer',
    'StoredSignalFilterSerializer',
    'PrivateCategorySerializer',
    'PublicQuestionSerializerDetail',
    'AbridgedChildSignalSerializer',

    'CountrySerializer',
    'CitySerializer',
    'CityObjectSerializer',
    'SignalCityObjectSerializerDetail',
    'SignalCityObjectSerializerList'
]
