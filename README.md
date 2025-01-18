installation from git:

    pip install lucasjkr@git+https://github.com/lucasjkr/lucasjkr-test

usage:

    import lucasjkr as graph
    
    token = graph.bearer_token(
                client_id, 
                secret,
                tenant_id,
                scopes)
