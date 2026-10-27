
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models

app = FastAPI(
    title="Raízes do Nordeste",
    description="Cadastro de produtos",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


# Conexao com o banco de dados
def obter_banco():
    banco = SessionLocal()
    try:
        yield banco
    finally:
        banco.close()


# Inicio da API
@app.get("/")
def inicio():
    return {
        "mensagem": "API Raizes do Nordeste funcionando!"
    }


# CREATE - Cadastrar produto
@app.post("/produtos")
def criar_produto(
    nome: str,
    preco: float,
    descricao: str = "",
    disponivel: bool = True,
    banco: Session = Depends(obter_banco)
):
    produto = models.Produto(
        nome=nome,
        preco=preco,
        descricao=descricao,
        disponivel=disponivel
    )

    banco.add(produto)
    banco.commit()
    banco.refresh(produto)

    return produto


# READ - Listar produtos
@app.get("/produtos")
def listar_produtos(banco: Session = Depends(obter_banco)):
    return banco.query(models.Produto).all()


# READ - Consultar um produto
@app.get("/produtos/{produto_id}")
def consultar_produto(
    produto_id: int,
    banco: Session = Depends(obter_banco)
):
    produto = banco.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")

    return produto


# UPDATE - Atualizar produto
@app.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    nome: str,
    preco: float,
    descricao: str = "",
    disponivel: bool = True,
    banco: Session = Depends(obter_banco)
):
    produto = banco.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")

    produto.nome = nome
    produto.preco = preco
    produto.descricao = descricao
    produto.disponivel = disponivel

    banco.commit()
    banco.refresh(produto)

    return produto


# DELETE - Excluir produto
@app.delete("/produtos/{produto_id}")
def excluir_produto(
    produto_id: int,
    banco: Session = Depends(obter_banco)
):
    produto = banco.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if produto is None:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")

    banco.delete(produto)
    banco.commit()

    return {"mensagem": "Produto excluido com sucesso"}



# CREATE - Cadastrar pedido
@app.post("/pedidos")
def criar_pedido(
    unidade: str,
    produto: str,
    quantidade: int,
    banco: Session = Depends(obter_banco)
):
    if quantidade <= 0:
        raise HTTPException(
            status_code=400,
            detail="A quantidade deve ser maior que zero"
        )

    produto_cadastrado = banco.query(models.Produto).filter(
        models.Produto.nome.ilike(produto)
    ).first()

    if produto_cadastrado is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não cadastrado"
        )

    if not produto_cadastrado.disponivel:
        raise HTTPException(
            status_code=400,
            detail="Produto indisponível para venda"
        )

    # Calcular o total usando o preço cadastrado
    valor_total = produto_cadastrado.preco * quantidade

    pedido = models.Pedido(
        unidade=unidade,
        produto=produto_cadastrado.nome,
        quantidade=quantidade,
        valor_total=valor_total
    )

    banco.add(pedido)
    banco.commit()
    banco.refresh(pedido)

    return pedido
