from fabric.api import local, lcd


def build():
    with lcd("..\\reveal-show\\reveal-deeplearning"):
        local("xcopy deeplearning-slides.html ..\East196.github.io\dlshow\index.html")
        local("xcopy assets ..\East196.github.io\dlshow\ /s /e")
        local("xcopy revealjs_deps ..\East196.github.io\dlshow\ /s /e")

    with lcd("..\\nltk-book-2nd"):
        local("fab build")

    with lcd("..\oxford-cs-deepnlp-2017"):
        local("fab build")

    with lcd("..\stanford-cs224n-winter-2017"):
        local("fab build")
    # local("jupyter nbconvert docs/**/*.ipynb --to markdown")
    local("copy README.md docs\index.md")
    local("mkdocs build")
    local("xcopy site ..\East196.github.io\ /s /e")


def serve():
    local("mkdocs serve")
