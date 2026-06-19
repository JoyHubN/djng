from django.test import TestCase, Client
from django.urls import reverse
import json, os
from pathlib import Path

class ComprehensiveURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_comprehensive_urls(self):
        # Список путей для проверки: (url_name, args, kwargs, method, data)
        test_cases = [
            ('admin:index', None, None, 'GET', None),
            ('music:index', None, None, 'GET', None),
            ('music:categories', None, {'genre': 'rock'}, 'GET', None),
            ('music:rock_tracks', None, None, 'GET', None),
            ('music:rock', None, None, 'GET', None),
            ('users:login', None, None, 'POST', {'username': 'user', 'password': 'password'}),
            ('users:register', None, None, 'POST', {'username': 'newuser', 'password': 'password'}),
            ('profile:main', None, None, 'GET', None),
            ('api_v1:filter', None, None, 'POST', {'filter_data': 'test_value'}),
        ]
        
        results = []
        for name, args, kwargs, method, data in test_cases:
            try:
                url = reverse(name, args=args, kwargs=kwargs)
                if method == 'GET':
                    response = self.client.get(url)
                elif method == 'POST':
                    response = self.client.post(url, data=data, content_type='application/json')
                
                results.append(f"{url} ({method}): {response.status_code}")
            except Exception as e:
                results.append(f"{name} ({method}): ERROR - {str(e)}")
        

        # print(f'========={=}')
        with open(f"{Path(os.getcwd(), 'test_results', 'comprehensive_test_result.txt')}", 'w') as f:
            for line in results:
                f.write(line + '\n')
