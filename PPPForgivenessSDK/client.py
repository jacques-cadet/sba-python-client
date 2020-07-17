
from .document_types import DocumentTypeApi
from .loan_documents import LoanDocumentsApi
from .forgiveness import ForgivenessRequestApi
from .messages import MessageApi


class Client(object):
    version = 'v1'
    environments = {
        'production': 'https://app.ussbaforgiveness.com/',
        'sandbox': 'https://sandbox.ussbaforgiveness.com/',
        'perf': 'https://perf.ussbaforgiveness.com/',
    }

    def __init__(self, timeout=60, max_retries=3, backoff_factor=0,
                 environment='production', access_token=None,
                 vendor_key=None, extra_headers={}):
        """The base class to instantiate to access the API

        :param timeout: The value to use for the connection timeout
        :param max_retries: The number of times to retry connecting to the endpoint
        :param backoff_factor: A backoff factor to apply between attempts after the second try
        :param environment: Current API environment
        :param access_token: OAuth 2.0 Access Token
        :param extra_headers: Additional headers to apply to all requests
        """

        assert access_token is not None
        if environment == 'production':
            assert vendor_key is not None

        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.environment = environment
        self.access_token = access_token
        self.vendor_key = vendor_key
        self.extra_headers = extra_headers

    @property
    def base_uri(self):
        """Generates the base URI for the selected environment

            :return:
                str: The base URI
        """

        return self.environments[self.environment]

    @property
    def api_uri(self):
        """Generates the auth URI for retrieving an auth token
                    :return:
                        str: The auth URI
                """
        return self.base_uri + 'api/'

    @property
    def forgiveness_requests(self):
        return ForgivenessRequestApi(self)

    @property
    def document_types(self):
        return DocumentTypeApi(self)

    @property
    def loan_documents(self):
        return LoanDocumentsApi(self)

    @property
    def messages(self):
        return MessageApi(self)

