vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

vim.keymap.set("n", "J", "mzJ`z")
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

vim.keymap.set("n", "<leader>vwm", function()
  require("vim-with-me").StartVimWithMe()
end)
vim.keymap.set("n", "<leader>svwm", function()
  require("vim-with-me").StopVimWithMe()
end)

-- remaps for folding
vim.keymap.set('n', '<space>', 'za', { noremap = true })
vim.keymap.set('v', '<space>', 'zf', { noremap = true })
vim.keymap.set('n', 'z1', ':set foldlevel=0<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z2', ':set foldlevel=1<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z3', ':set foldlevel=2<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z4', ':set foldlevel=3<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z5', ':set foldlevel=4<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z6', ':set foldlevel=5<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z7', ':set foldlevel=6<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z8', ':set foldlevel=7<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z9', ':set foldlevel=8<CR><Esc>', { noremap = true })
vim.keymap.set('n', 'z0', ':set foldlevel=99<CR><Esc>', { noremap = true })

-- Change the window bindings
vim.keymap.set('n', '<C-up>', '<C-w>k', { noremap = true })
vim.keymap.set('n', '<C-down>', '<C-w>j', { noremap = true })
vim.keymap.set('n', '<C-left>', '<C-w>h', { noremap = true })
vim.keymap.set('n', '<C-right>', '<C-w>l', { noremap = true })
vim.keymap.set('n', '<C-h>', '<C-w>h', { noremap = true })
vim.keymap.set('n', '<C-j>', '<C-w>j', { noremap = true })
vim.keymap.set('n', '<C-k>', '<C-w>k', { noremap = true })
vim.keymap.set('n', '<C-l>', '<C-w>l', { noremap = true })



-- greatest remap ever
vim.keymap.set("x", "<leader>p", [["_dP]])

-- next greatest remap ever : asbjornHaland
vim.keymap.set({"n", "v"}, "<leader>y", [["+y]])
vim.keymap.set("n", "<leader>Y", [["+Y]])

vim.keymap.set({"n", "v"}, "<leader>d", [["_d]])

-- This is going to get me cancelled
vim.keymap.set("i", "<C-c>", "<Esc>")

vim.keymap.set("n", "Q", "<nop>")
vim.keymap.set("n", "<C-f>", "<cmd>silent !tmux neww tmux-sessionizer<CR>")
vim.keymap.set("n", "<leader>f", vim.lsp.buf.format)

vim.keymap.set("n", "<C-k>", "<cmd>cnext<CR>zz")
vim.keymap.set("n", "<C-j>", "<cmd>cprev<CR>zz")
vim.keymap.set("n", "<leader>k", "<cmd>lnext<CR>zz")
vim.keymap.set("n", "<leader>j", "<cmd>lprev<CR>zz")

vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })

vim.keymap.set("n", "<leader>vpp", "<cmd>e ~/.dotfiles/nvim/.config/nvim/lua/theprimeagen/packer.lua<CR>");
vim.keymap.set("n", "<leader>mr", "<cmd>CellularAutomaton make_it_rain<CR>");

vim.keymap.set("n", "<leader><leader>", function()
  vim.cmd("so")
end)

