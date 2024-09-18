import unittest
from unittest.mock import patch
from src.terminal_nmap import main_screen, option1_screen, option2_screen

class TestMainScreenIntegration(unittest.TestCase):

    @patch('src.terminal_nmap.Prompt.ask')
    @patch('src.terminal_nmap.option1_screen')
    def test_scan_current_network_flow(self, mock_option1_screen, mock_prompt):
        # Simular entradas do usuário
        mock_prompt.side_effect = ['1', 'Q']

        # Chamar a função principal
        main_screen()

        # Verificar se option1_screen foi chamada
        mock_option1_screen.assert_called_once()

    @patch('src.terminal_nmap.Prompt.ask')
    @patch('src.terminal_nmap.option2_screen')
    def test_scan_host_flow(self, mock_option2_screen, mock_prompt):
        # Simular entradas do usuário
        mock_prompt.side_effect = ['2', 'Q']

        # Chamar a função principal
        main_screen()

        # Verificar se option2_screen foi chamada
        mock_option2_screen.assert_called_once()

if __name__ == '__main__':
    unittest.main()
