function copiarSenha() {
    const senha = document.getElementById('senhaGerada').innerText;
    navigator.clipboard.writeText(senha).then(() => {
        alert("Senha copiada com sucesso!");
    }).catch(err => {
        alert("Erro ao copiar a senha.");
        console.error(err);
    });
}
