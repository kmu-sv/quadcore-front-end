from quadcore import oauth

class AuthManager:

    oauth_github = oauth.remote_app(
        'github',
        consumer_key='Iv1.2ce83a98d79af095',
        consumer_secret='05316b10734d10fa53790d109f8ddc7484e8758e',
        request_token_params={'scope': 'user:email'},
        base_url='https://api.github.com/',
        request_token_url=None,
        access_token_method='POST',
        access_token_url='https://github.com/login/oauth/access_token',
        authorize_url='https://github.com/login/oauth/authorize',
        redirect_uri='http://quadcore.news/profile'
    )

    @oauth_github.tokengetter
    def get_github_oauth_token():
        return session.get('github_token')

    # def change_linkedin_query(uri, headers, body):
    #     auth = headers.pop('Authorization')
    #     headers['x-li-format'] = 'json'
    #     if auth:
    #         auth = auth.replace('Bearer', '').strip()
    #         if '?' in uri:
    #             uri += '&oauth2_access_token=' + auth
    #         else:
    #             uri += '?oauth2_access_token=' + auth
    #     return uri, headers, body

    # @classmethod
    # def get_cred_from_linkedin(cls, username):
    #     """
    #     Get credentials from LinkedIn.
    #     """
    
