import browser_cookie3
from tkinter import filedialog
from main_infos_impor import infoLocalizacao_Coockies, caminho_pasta_download

def salvar_cookies_netscape(cookies, arquivo_cooockies):

    with open(arquivo_cooockies, "w", encoding="utf-8") as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# Gerado automaticamente por script\n\n")

        for c in cookies:
            domain = c.domain
            include_subdomains = "TRUE" if domain.startswith(".") else "FALSE"
            path = c.path or "/"
            secure = "TRUE" if c.secure else "FALSE"
            expires = str(c.expires or 0)
            name = c.name
            value = c.value

            linha = f"{domain}\t{include_subdomains}\t{path}\t{secure}\t{expires}\t{name}\t{value}\n"
            f.write(linha)

    print(f"[✅] Arquivo salvo em: {infoLocalizacao_Coockies}")

def iniciar():
    cj = browser_cookie3.chrome(domain_name="youtube.com")
    salvar_cookies_netscape(cj, infoLocalizacao_Coockies)
if __name__ == "__main__":
    iniciar()

def Verificacao_Pasta(caminho_pasta, mudar):
    if mudar == True:

        pasta_download = filedialog.askdirectory(title= 'Selecione uma pasta de download')
        with open(caminho_pasta, "w", encoding="utf-8") as c:
            c.write(pasta_download)
        return pasta_download

    else:

        with open(caminho_pasta, "r", encoding="utf-8") as f:
            var = f.read()
            if var:
                pass
                return var
            else:
                print("Nenhuma pasta detectada. Selecione uma pasta de download")
                pasta_download = filedialog.askdirectory(title= 'Selecione uma pasta de download')
                with open(caminho_pasta, "w", encoding="utf-8") as b:
                    b.write(pasta_download)
                return pasta_download
