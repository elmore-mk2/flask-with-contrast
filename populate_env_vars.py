import yaml

import os


def main():

    with open('contrast_security_templ.yml') as file:
        conf = yaml.safe_load(file)
        conf['api']['url'] = os.getenv('CONTRAST_URL')
        conf['api']['api_key'] = os.getenv('CONTRAST_API_KEY')
        conf['api']['service_key'] = os.getenv('CONTRAST_SERVICE_KEY')
        conf['api']['user_name'] = os.getenv('CONTRAST_USER_NAME')

    print(os.getenv('FLASK_APP'))
    print(os.getenv('FLASK_ENV'))
    with open('contrast_security.yaml', 'a') as file:
        yaml.dump(conf, file)


if __name__ == '__main__':
    main()
