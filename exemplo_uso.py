"""
Exemplo de uso do sistema de cadastro de usuários.
Execute este arquivo para testar o sistema manualmente.
"""

import sys
sys.path.insert(0, 'src')

from user_system import SistemaCadastro

def main():
    """Demonstra o uso do sistema de cadastro."""
    
    # Cria uma instância do sistema
    sistema = SistemaCadastro()
    
    print("=" * 50)
    print("Sistema de Cadastro de Usuários - Demonstração")
    print("=" * 50)
    print()
    
    # Testa cadastro válido
    print("1. Testando cadastro válido...")
    sucesso, msg = sistema.cadastrar_usuario("usuario@exemplo.com", "senha123")
    print(f"   Resultado: {msg}")
    print()
    
    # Testa cadastro inválido (e-mail)
    print("2. Testando cadastro com e-mail inválido...")
    sucesso, msg = sistema.cadastrar_usuario("email_invalido", "senha123")
    print(f"   Resultado: {msg}")
    print()
    
    # Testa cadastro inválido (senha)
    print("3. Testando cadastro com senha inválida...")
    sucesso, msg = sistema.cadastrar_usuario("teste@exemplo.com", "abc12")
    print(f"   Resultado: {msg}")
    print()
    
    # Cadastra mais alguns usuários válidos
    print("4. Cadastrando mais usuários válidos...")
    sistema.cadastrar_usuario("admin@empresa.com", "admin123")
    sistema.cadastrar_usuario("cliente@loja.com", "cliente456")
    print("   Usuários cadastrados com sucesso!")
    print()
    
    # Busca usuário
    print("5. Buscando usuário cadastrado...")
    usuario = sistema.buscar_usuario("usuario@exemplo.com")
    if usuario:
        print(f"   ✓ Usuário encontrado: {usuario.email}")
    else:
        print("   ✗ Usuário não encontrado")
    print()
    
    # Busca usuário inexistente
    print("6. Buscando usuário inexistente...")
    usuario = sistema.buscar_usuario("naoexiste@teste.com")
    if usuario:
        print(f"   ✓ Usuário encontrado: {usuario.email}")
    else:
        print("   ✗ Usuário não encontrado (esperado)")
    print()
    
    # Mostra histórico
    print("7. Histórico de usuários:")
    historico = sistema.obter_historico()
    print(f"   Total de usuários cadastrados: {sistema.contar_usuarios()}")
    for i, usuario in enumerate(historico, 1):
        print(f"   {i}. {usuario.email}")
    print()
    
    print("=" * 50)
    print("Demonstração concluída!")
    print("=" * 50)

if __name__ == '__main__':
    main()

