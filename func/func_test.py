import subprocess
import time
from nose2.compat import unittest

from selenium import webdriver

from womack.publish import Publisher


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = subprocess.Popen(
            ['womack'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        time.sleep(2)
        cls.ffox = webdriver.Firefox()
        cls.ffox2 = webdriver.Firefox()
        cls.ffox3 = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.ffox.close()
        cls.ffox2.close()
        cls.ffox3.close()
        cls.server.kill()

    def setUp(self):
        self.womack = Publisher()

    def test_hello_world(self):
        self.ffox.get('http://localhost:8111/test.html')
        time.sleep(2)
        self.womack.publish('hello', {"hello": "world"})
        time.sleep(.1)
        log = self.ffox.find_element_by_id('log')
        assert 'hello world' in log.text, "hello world not found: %s" % log.text

    def test_multiple_clients_one_channel(self):
        self.subscribe('test1', self.ffox, self.ffox2, self.ffox3)
        for i in range(0, 100):
            self.womack.publish(
                'test1', {'message': i, 'timestamp': time.time()})
        time.sleep(2)
        # +3 because two startup messages always included
        # and range is not end-inclusive
        self.assertReceivedAll(i+3, self.ffox, self.ffox2, self.ffox3)

    def test_multiple_clients_different_channels(self):
        self.subscribe('a1', self.ffox)
        self.subscribe('a2', self.ffox2)
        self.subscribe('a3', self.ffox3)
        for ch, num in (('a1', 4), ('a2', 7), ('a3', 2)):
            for i in range(0, num):
                self.womack.publish(
                    ch, {'message': i, 'timestamp': time.time()})
        time.sleep(2)
        # +2 because two startup messages always included
        self.assertReceivedAll(6, self.ffox)
        self.assertReceivedAll(9, self.ffox2)
        self.assertReceivedAll(4, self.ffox3)

    def assertReceivedAll(self, num, *browsers):
        for browser in browsers:
            nth = browser.find_elements_by_css_selector('#log li')
            self.assertEqual(
                len(nth), num,
                "%s received %s messages not %s" % (
                    browser, len(nth), num))
            times = [float(n.find_elements_by_tag_name('span')[2].text)
                     for n in nth[3:]]
            avg = sum(times)/len(times)
            m = max(times)
            self.assertLess(avg, 0.2, '%s avg time (%s) over .2 seconds!' % (
                    browser, avg))
            self.assertLess(m, 1.0, '%s max time (%s) over 1 second!' % (
                    browser, avg))

    def subscribe(self, channel, *browsers):
        for browser in browsers:
            browser.get('http://localhost:8111/channel_test.html')
            inp = browser.find_element_by_id('channel')
            inp.clear()
            inp.send_keys(channel)
            browser.find_element_by_id('set-channel').click()


class TestCrossOrigin(unittest.TestCase):
    """Tests fetching application code from one port w/sockets on another"""
    @classmethod
    def setUpClass(cls):
        cls.server1 = subprocess.Popen(
            ['womack'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        cls.server2 = subprocess.Popen(
            ['womack', '-p', '8080'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        time.sleep(2)
        cls.ffox = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.ffox.close()
        cls.server1.kill()
        cls.server2.kill()

    def setUp(self):
        self.womack = Publisher()

    def test_hello_world(self):
        self.ffox.get('http://localhost:8080/test.html')
        time.sleep(2)
        self.womack.publish('hello', {"hello": "world"})
        time.sleep(.1)
        log = self.ffox.find_element_by_id('log')
        assert 'hello world' in log.text, "hello world not found: %s" % log.text
