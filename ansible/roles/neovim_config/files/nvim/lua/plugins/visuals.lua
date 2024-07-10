return
  {
    -- vim-airline
    {
      "vim-airline/vim-airline",
      tag = "v0.11",
      lazy = false
    },

    {
      "vim-airline/vim-airline-themes",
      lazy = false
    },

    -- colors
    {
      "rose-pine/neovim",
      tag = "v3.0.1",
      name = "rose-pine",
      config = function()
        vim.cmd.colorscheme("rose-pine")
        vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
        vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
      end
    }
  }
