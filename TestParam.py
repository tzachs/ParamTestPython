import unittest
import json

class TestParam(unittest.TestCase):

	def setUp(self):
		with open('data.json') as data_file:
			self.data = json.load(data_file)
		print "Setup"

	def test_loop(self):
		for item in self.data["tests"]:
			print item["name"]
			self.assertEqual(item["number1"] + item["number2"], item["result"])


if __name__ == '__main__':
	unittest.main()
