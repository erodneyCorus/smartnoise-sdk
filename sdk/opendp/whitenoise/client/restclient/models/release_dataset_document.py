# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReleaseDatasetDocument(Model):
    """ReleaseDatasetDocument.

    :param dataset_name: The name for the dataset
    :type dataset_name: str
    :param dataset_type: The type of the dataset
    :type dataset_type: str
    :param budget: Available budget for the dataset registered
    :type budget: float
    :param authorized_users:
    :type authorized_users: list[str]
    :param csv_details:
    :type csv_details: ~restclient.models.LocalCSVDetails
    :param dataverse_details:
    :type dataverse_details: ~restclient.models.DataverseDetails
    """

    _attribute_map = {
        'dataset_name': {'key': 'dataset_name', 'type': 'str'},
        'dataset_type': {'key': 'dataset_type', 'type': 'str'},
        'budget': {'key': 'budget', 'type': 'float'},
        'authorized_users': {'key': 'authorized_users', 'type': '[str]'},
        'csv_details': {'key': 'csv_details', 'type': 'LocalCSVDetails'},
        'dataverse_details': {'key': 'dataverse_details', 'type': 'DataverseDetails'},
    }

    def __init__(self, dataset_name=None, dataset_type=None, budget=None, authorized_users=None, csv_details=None, dataverse_details=None):
        super(ReleaseDatasetDocument, self).__init__()
        self.dataset_name = dataset_name
        self.dataset_type = dataset_type
        self.budget = budget
        self.authorized_users = authorized_users
        self.csv_details = csv_details
        self.dataverse_details = dataverse_details
