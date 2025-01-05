import logging, msal

class SimpleMsAuth:

    def bearer_token(self, client_id, tenant_id, secret, scopes):
        # code for retrieving a Graph token, slightly adapted from Microsofts example code
        app = msal.ConfidentialClientApplication(
            client_id,
            authority="https://login.microsoftonline.com/" + tenant_id,
            client_credential=secret,
        )
        result = app.acquire_token_silent(scopes, account=None)
        if not result:
            logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
            result = app.acquire_token_for_client(scopes=scopes)

        if "access_token" in result:
            logging.info("Authentication succeeded. Token acquired")
            return result["access_token"]

        else:
            e = "Authentication failed: " + result.get("error_description", "No error description available")
            logging.critical(e)
            raise Exception(e)