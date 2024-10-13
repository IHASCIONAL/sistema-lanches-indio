import streamlit as st
from backend import produtos

class HeaderDisplay:
    def __init__(self, title="Cadastro de Pedidos", subtitle=None):
        self.title = title
        self.subtitle = subtitle

    def display(self):
        st.title(self.title)
        if self.subtitle:
            st.subheader(self.subtitle)

class ProductManager:
    def __init__(self):
        self.produtos_loja = produtos.ListaProdutos()

    def get_produtos_formatados(self):
        produtos_dict = {
            f"{codigo} - {detalhes['nome']}": detalhes
            for codigo, detalhes in self.produtos_loja.menu.items()
        }
        return produtos_dict

class ProductSelection:
    def __init__(self, product_manager):
        self.product_manager = product_manager

    def display_selection(self):
        produtos_dict = self.product_manager.get_produtos_formatados()

        col1, col2 = st.columns(2)

        with col1:
            option = st.selectbox(
                "Selecione o código do produto vendido!",
                list(produtos_dict.keys()),
                key="product_selectbox"
            )

        with col2:
            quantidade = st.number_input("Quantos produtos iguais a esse?", 
                                         min_value=1, 
                                         step=1, 
                                         key="quantity_input")

        if st.button("Confirmar Seleção"):
            produto_selecionado = produtos_dict[option]
            valor_total = quantidade * produto_selecionado['preço']

            st.write(f"""Você está cadastrando {quantidade} "{produto_selecionado['nome']}", no valor de R$ {valor_total:.2f}.""")

            # Adicionar ao carrinho
            if 'carrinho' not in st.session_state:
                st.session_state.carrinho = []
            
            st.session_state.carrinho.append({
                'produto': produto_selecionado['nome'],
                'quantidade': quantidade,
                'valor_total': valor_total
            })

            st.success("Produto adicionado à lista!")

class CartDisplay:
    def display(self):
        if 'carrinho' not in st.session_state:
            st.session_state.carrinho = []

        if 'remove_index' in st.session_state:
            st.session_state.carrinho.pop(st.session_state.remove_index)
            del st.session_state.remove_index

        if st.session_state.carrinho:
            st.subheader("Lista de Vendas")
            
            for index, item in enumerate(st.session_state.carrinho):
                col1, col2, col3 = st.columns([3, 1, 1])
                
                with col1:
                    st.write(f"{item['quantidade']} unidade(s) {item['produto']} - R$ {item['valor_total']:.2f}")
                
                with col2:
                    if st.button(f"Remover", key=f"remove_{index}"):
                        st.session_state.remove_index = index
                        st.rerun()
                
                with col3:
                    if st.button(f"Editar", key=f"edit_{index}"):
                        st.session_state.editing_item = index
                
                if 'editing_item' in st.session_state and st.session_state.editing_item == index:
                    new_quantity = st.number_input("Nova quantidade", min_value=1, value=item['quantidade'], key=f"edit_quantity_{index}")
                    if st.button("Confirmar edição", key=f"confirm_edit_{index}"):
                        item['quantidade'] = new_quantity
                        item['valor_total'] = new_quantity * (item['valor_total'] / item['quantidade'])
                        del st.session_state.editing_item
                        st.rerun()
            
            total = sum(item['valor_total'] for item in st.session_state.carrinho)
            st.write(f"Total: R$ {total:.2f}")

            if st.button("Limpar a lista inteira"):
                st.session_state.carrinho = []
                st.rerun()

        else:
            st.info("A lista está vazia!")

class OrderPage:
    def __init__(self):
        self.header = HeaderDisplay()
        self.product_manager = ProductManager()
        self.product_selection = ProductSelection(self.product_manager)
        self.cart_display = CartDisplay()

    def render(self):
        self.header.display()
        self.product_selection.display_selection()
        self.cart_display.display()
