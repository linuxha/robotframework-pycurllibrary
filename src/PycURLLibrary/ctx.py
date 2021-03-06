'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''
'''
Created on 30 May 2013

@author: Markku Saarela
'''
import xml.etree.ElementTree as ET

class Ctx(object):
    def __init__(self):
        self._url = None
        self._response = None
        self._capath = None
        self._client_certificate_file = None
        self._private_key_file = None
        self._headers = []
        self._response_headers = None
        self._protocol = None
        self._request_method = 'GET'
        self._response_status = None
        self._server_connection_establishment_timeout = None
        self._xml_root_element = None
        
    def get_url(self):
        return self._url

    def set_url(self, url):
        self._url = url
        self._parse_protocol(url)
        
    def get_server_connection_establishment_timeout(self):
        return self._server_connection_establishment_timeout
        
    def set_server_connection_establishment_timeout(self, timeout):
        self._server_connection_establishment_timeout = timeout
        
    def get_capath(self):
        return self._capath
    
    def set_capath(self, capath):
        self._capath = capath
    
    def get_client_certificate_file(self):
        return self._client_certificate_file
    
    def set_client_certificate_file(self, client_certificate_file):
        self._client_certificate_file = client_certificate_file
    
    def get_private_key_file(self):
        return self._private_key_file
    
    def set_private_key_file(self, private_key_file):
        self._private_key_file = private_key_file
    
    def get_request_method(self):
        return self._request_method

    def set_request_method(self, requestMethod):
        self._request_method = requestMethod

    def add_header(self, header):
        self.get_headers().append(header)
        
    def get_headers(self):
        return self._headers
        
    def set_headers(self, headers):
        self._headers = headers
        
    def get_response(self):
        return self._response

    def set_response(self, response):
        self._response = response

    def get_response_headers(self):
        return self._response_headers

    def set_response_headers(self, responseHeaders):
        if responseHeaders is None:
            self._response_headers = None
            self._response_status = None
        else:
            self._response_headers = responseHeaders.splitlines()
            self._response_status = self._parseResponseLine()
        
    def get_response_status(self):
        return self._response_status

    def get_protocol(self):
        return self._protocol
    
    def parse_response_xml(self): 
        self._xml_root_element = ET.fromstring(self.get_response())
        return self.get_xml_root_element()
    
    def get_xml_root_element(self):
        return self._xml_root_element

    def _parse_protocol(self, url):
        i = url.find(':')
        self._protocol = url[0:i].upper()
        
    def _parseResponseLine(self):
        isHttpStatusLine = self._response_headers[0].startswith('HTTP')
        if isHttpStatusLine:
            statusLine = self._response_headers[0].split()
            return '{0} {1}'.format(statusLine[1], statusLine[2])
        else:
            return None
