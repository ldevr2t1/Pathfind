#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API developed for the pathfinding storage. To start, post to root to obtain a UID and then post away using the UID'})
    app.run(host='ec2-35-167-218-237.us-west-2.compute.amazonaws.com', port=8080)
