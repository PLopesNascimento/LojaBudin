import streamlit as st
import sqlite3

banco=sqlite3.connect("vendas.db")
b = banco.cursor()

def criarTabelaCat():
    b.execute('CREATE TABLE IF NOT EXISTS categoria(produto TEXT)')

def salvarBdCat(produto):
    b.execute('INSERT INTO categoria(produto)VALUES(?)',(produto,))
    banco.commit()
def viewCat():
    b.execute('SELECT * FROM categoria')
    data=b.fetchall()
    return data
###----------------------------------------------------------------------
# Layout Templates



def main():
    st.title("Controle Vendas")
    financeiro=["Vendas", "Compras","Cadastro","Pesquisa"]
    opcao = st.sidebar.selectbox("Financeiro",financeiro)

    if opcao=="Vendas":
        st.subheader("Vendas")
    elif opcao == "Compras":
        st.subheader("Compras")



    elif opcao == "Cadastro":
        cad = ["Categoria","Produto","Fornecedor"]
        opcaoCad = st.selectbox("Cadastros",cad)
        if opcaoCad == "Categoria":
            #xst.subheader("Cadastro")
            criarTabelaCat()
            produtoCat = st.text_input("Nome da Categoria", max_chars=50)
            if st.button("Salvar"):
                salvarBdCat(produtoCat)
                resultado = viewCat()
                for i in resultado:
                        st.write(i)
                st.success("Dados Cadastrado")


    elif opcao=="Pesquisa":
        st.subheader("Pesquisa")




if __name__=='__main__':
    main()