return
  {
    {
      "preservim/nerdtree",
      tag = "7.1.2",
    },

    {
      "nvim-treesitter/nvim-treesitter",
      tag = "v0.9.2",
      build = ":TSUpdate",
      config = function()
        local configs = require ("nvim-treesitter.configs")
        configs.setup(
          {
            ensure_installed = {"lua", "vimdoc"},
            ignore_install = {},
            sync_install = false,
            auto_install = false,
            highlight =
              {
                enable = true,
                additional_vim_regex_highlighting = false,
              },
            indent = { enable = true },
            fold = { enable = true }
          })
      end
    },

    {
      "nvim-telescope/telescope.nvim",
      tag = '0.1.8',
      dependencies =
        {
          "nvim-lua/plenary.nvim",
          tag = "v0.1.4",
        },
      config = function()
        local builtin = require("telescope.builtin")
        vim.keymap.set("n", "<leader>pf", builtin.find_files, {})
        vim.keymap.set("n", "<C-p>", builtin.git_files, {})
        vim.keymap.set("n", "<leader>ps",
          function()
            builtin.grep_string({ search = vim.fn.input("Grep > ") });
          end)
      end
    },

    {
      "theprimeagen/harpoon",
      config = function()
        local mark = require("harpoon.mark")
        local ui = require("harpoon.ui")

        vim.keymap.set("n", "<leader>a", mark.add_file)
        vim.keymap.set("n", "<C-e>", ui.toggle_quick_menu)

        vim.keymap.set("n", "<C-h>", function() ui.nav_file(1) end)
        vim.keymap.set("n", "<C-t>", function() ui.nav_file(2) end)
        vim.keymap.set("n", "<C-n>", function() ui.nav_file(3) end)
        vim.keymap.set("n", "<C-s>", function() ui.nav_file(4) end)
      end
    },

    {
      "mbbill/undotree",
      tag = "rel_6.1",
      config = function()
        vim.keymap.set('n', '<leader>u', vim.cmd.UndotreeToggle)
      end
    },

    {
      "tpope/vim-fugitive",
      tag = "v3.7",
      config = function()
        vim.keymap.set("n", "<leader>gs", vim.cmd.Git)
      end
    },

  }
