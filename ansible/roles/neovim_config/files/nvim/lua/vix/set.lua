vim.opt.relativenumber = true
vim.opt.number = true

vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2
vim.opt.expandtab = true

vim.opt.smartindent = true

vim.opt.wrap = false

-- Esc button delay configuration
-- Link: https://vi.stackexchange.com/questions/16148/slow-vim-escape-from-insert-mode
vim.opt.timeoutlen=1000
vim.opt.ttimeoutlen=5

vim.opt.swapfile = false
vim.opt.backup = false
vim.opt.undodir = os.getenv("HOME") .. "/.local/var/undodir"
vim.opt.undofile = true

vim.opt.hlsearch = false
vim.opt.incsearch = true

vim.opt.termguicolors = true

vim.opt.scrolloff = 8
vim.opt.signcolumn = "yes"
vim.opt.isfname:append("@-@")

vim.opt.updatetime = 50

-- adds a colored divider
-- vim.opt.colorcolumn = "80"
-- Clear trailing whitespace

vim.cmd([[command! CLS %s/\s\+$//]])
vim.api.nvim_set_keymap('n', '<leader>cl', ':CLS<CR>', {noremap = true})

-- Fuzzy file search in vim without plugin
-- Link: https://www.youtube.com/watch?v=XA2WjJbmmoM&t=3482s
-- Search down into subfolders
vim.opt.path:append("**")

-- Display all matching files when pressing tab
vim.opt.wildmenu = true

-- Folding settings
vim.opt.foldmethod = 'expr'
vim.opt.foldexpr = 'nvim_treesitter#foldexpr()'
vim.opt.foldlevel = 99

-- Disable unnessarary providers
vim.g.loaded_ruby_provider = 0
vim.g.loaded_node_provider = 0
vim.g.loaded_perl_provider = 0

