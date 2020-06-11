library(reticulate)
Sys.setenv(RETICULATE_PYTHON = conda_python())

## Default Configurations ----
knitr_config <- list(
  fig.width   = 12, 
  fig.asp     = 0.618, 
  fig.align   = "center",
  fig.path    = "Figure/",
  engine      = "python",
  background  = NA,
  comment     = NA
)

## Specific for Mac ----
if (Sys.info()["sysname"] %in% c("Darwin")) {
  knitr_config[['engine.path']] <- list(python = conda_python())
}

## Set printer-friendly knitr theme, run only when called from LyX ----
if (!interactive()){
    thm <- knitr::knit_theme$get("print")
    knitr::knit_theme$set(thm)
}

knitr::opts_chunk$set(knitr_config)

## Common Hooks ----
hook_lst_bf <- function(x, options) {
    paste("\\begin{lstlisting}[basicstyle={\\bfseries}]\n", x, 
        "\\end{lstlisting}\n", sep = "")
}

## Extract Option from Label
read_label <- function(lbl, split = '/') {
    label <- strsplit(lbl, split)[[1]]
    
    new_options <- list()
    if (length(label) < 3) return(new_options)
    
    if (label[[3]] == 'dnr') {
        new_options$eval <- FALSE
    } else if (label[[3]] == 'noinc') {
        new_options$include <- FALSE
    } else if (label[[3]] == 'graphics') {
        new_options$include <- FALSE
        new_options$fig.show <- 'hide'
    } else if (label[[3]] == 'plot') {
        new_options$fig.show <- 'hide'
        new_options$echo <- TRUE
    }
    new_options$label <- paste0(label[[1]], '/', label[[2]])
    new_options
}

## Customize Hooks ----
knitr::knit_hooks$set(
    sympy = function(before, options, envir) {},
    source = function(x, options) {
        if (!is.null(options$sympy) && options$sympy){
            x <- sub("from\\s+sympy\\s+import\\s+latex\\n", "", x)
            x <- sub("print\\(latex\\((.*),(.*)\\)\\)", "\\1", x)
        }
        
        lst_opts <- "style=Source"
        if (!is.null(options$caption)) {
            lst_opts <- paste0(lst_opts, ",caption=", options$caption)
            lst_opts <- paste0(lst_opts, ",label=", options$fig.lp, options$label)
        }

        paste0("\\begin{lstlisting}[", lst_opts, "]\n",  
              paste(x, collapse="\n"), 
              "\n\\end{lstlisting}\n", sep = "")
    }, 
    output = function(x, options) {
        if (options$results == 'asis') return(x)
        paste("\\begin{lstlisting}[style=Result]\n", x, 
            "\\end{lstlisting}\n", sep = "")
    }, 
    chunk = function(x, options) x,
    warning = hook_lst_bf, 
    message = hook_lst_bf, 
    error = hook_lst_bf,
    document = function(x) {
        gsub('\\\\(begin|end)\\{kframe\\}', '', x)
    }
)

## Option Hooks ----
knitr::opts_hooks$set(
    # For SymPy Code
    sympy = function(options) {
        if(options$sympy) options$results = "asis"
        options
    },
    echo = function(options) {
        echo <- read_label(options$label)$echo
        if (!is.null(echo)) options$echo <- echo
        options
    },
    eval = function(options) {
        eval <- read_label(options$label)$eval
        if (!is.null(eval)) options$eval <- eval
        options
    },
    include = function(options) {
        include <- read_label(options$label)$include
        if (!is.null(include)) options$include <- include
        options
    },
    fig.show = function(options) {
        fig.show <- read_label(options$label)$fig.show
        if (!is.null(fig.show)) options$fig.show <- fig.show
        options
    },
    label = function(options) {
        label <- read_label(options$label)$label
        if (!is.null(label)) options$label <- label
        options
    }
)

## empty highlight header ----
knitr::set_header(highlight = "")

## Shims ----

shim_py_inject_r <- function(envir) {
    
    # define our 'R' class
    py_run_string("class R(object): pass")
    
    # extract it from the main module
    main <- import_main(convert = FALSE)
    R <- main$R
    
    # extract active knit environment
    if (is.null(envir)) {
        .knitEnv <- reticulate:::yoink("knitr", ".knitEnv")
        envir <- .knitEnv$knit_global
    }
    
    # define the getters, setters we'll attach to the Python class
    getter <- function(self, code) {
        object <- eval(parse(text = as_r_value(code)), envir = envir)
        r_to_py(object, convert = is.function(object))
    }
    
    setter <- function(self, name, value) {
        envir[[as_r_value(name)]] <<- as_r_value(value)
    }
    
    py_set_attr(R, "__getattr__", getter)
    py_set_attr(R, "__setattr__", setter)
    py_set_attr(R, "__getitem__", getter)
    py_set_attr(R, "__setitem__", setter)
    
    # now define the R object
    py_run_string("robj = R()")
    
}

utils::assignInNamespace("py_inject_r", shim_py_inject_r,
                         envir = as.environment("package:reticulate"))


