# from session import Session

DEFAULT_SESSION = None



# def setup_default_session(**kwargs):
#     global DEFAULT_SESSION
#     DEFAULT_SESSION = Session(**kwargs)
#
#
# def _get_default_session():
#     """
#     Get the default session, creating one if needed.
#
#     :rtype: :py:class:`~boto3.session.Session`
#     :return: The default session
#     """
#     if DEFAULT_SESSION is None:
#         setup_default_session()
#
#     return DEFAULT_SESSION
#
#
# def client(*args, **kwargs):
#     """
#     Create a low-level service client by name using the default session.
#
#     See :py:meth:`boto3.session.Session.client`.
#     """
#     return _get_default_session().client(*args, **kwargs)
