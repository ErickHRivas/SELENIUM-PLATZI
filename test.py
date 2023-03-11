import unittest # sirve para traer todas las pruebas
from pyunitreport import HTMLTestRunner # para orquestar cada una de las pruebas junto con los reportes
from selenium import webdriver # comunicar con el navegador

class HelloWorld( unittest.TestCase ):
  # prepara el entorno de la prueba misma
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome( executable_path = r'./chromedriver.exe' )
    driver = cls.driver
    driver.implicitly_wait(10)

  # caso de prueba
  def test_hello_world( self ):
    driver = self.driver
    driver.get('https://www.platzi.com')

  def test_visit_wikipedia( self ):
    driver = self.driver
    driver.get('https://www.wikipedia.org')

  # acciones para finalizar
  @classmethod
  def tearDownClass(cls):
    return cls.driver.quit()


if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
  # unittest.main( verbosity = 2, testRunner = HTMLTestRunner( output = 'reportes', report_name = 'hello-world-report' ) )