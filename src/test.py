from unittest.mock import Mock, MagicMock, patch, call
from terminal_nmap import scan_host
import unittest

class TestScanHost(unittest.TestCase):

    @patch('builtins.print') # Para substituir o print padrao do python
    def test_scan_host_range(self, mock_print):
        mock_scanner = MagicMock()

        mock_scanner.all_hosts.return_value = ['127.0.0.1']
        mock_scanner.__getitem__.return_value.all_protocols.return_value = ['tcp']
        mock_scanner.__getitem__.return_value.__getitem__.return_value.keys.return_value = ['80']
        mock_scanner.__getitem__.return_value.__getitem__.return_value.__getitem__.return_value = {'name': 'http', 'state': 'open'}

        scan_host('www.uol.com.br', '80-1000', mock_scanner)

        mock_scanner.scan.assert_called_once_with(hosts='www.uol.com.br', arguments='-p 80-1000')

        # Verificar o output da função
        calls = [call('Scanning network www.uol.com.br...'),
                 call('\nScan results for 127.0.0.1:'),
                 call('Protocol : tcp'),
                 call('port: 80 (http)'),
                 call('state: open')]
        mock_print.assert_has_calls(calls, any_order=True)
        
        """
        Cabe dizer que ao realizar o mock do Scanner, o segundo argumento passado na funcao scan_host, que é o 'ports', não é utilizado.
        Visto que no código, esse parâmetro é repassada para a chamada da função scan do nmap.
        Ao utilizar o mock, ainda que esses valores sejam passados, o retorno da função scan_host será sempre o mesmo.
        """

if __name__ == '__main__':
    unittest.main()