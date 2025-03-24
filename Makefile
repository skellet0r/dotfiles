.PHONY: install
install:
	stow --verbose --target=$$HOME --dotfiles -S .

.PHONY: uninstall
uninstall:
	stow --verbose --target=$$HOME --dotfiles -D .
