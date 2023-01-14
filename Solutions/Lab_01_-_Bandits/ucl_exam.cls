%%
%% This is file `ucl_exam.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% ucl_exam.dcl 
%% 
%% IMPORTANT NOTICE:
%% 
%% For the copyright see the source file.
%% 
%% You are *not* allowed to modify this file.
%% 
%% You are *not* allowed to distribute this file.
%% For distribution of the original source see the terms
%% for copying and modification in the file ucl_exam.dcl.
%% 
%%  A LaTeX2e class for UCL examination papers.
%%
%%  Copyright (c) 1996, Russel Winder and Sean Holden.
%%
\def \fileversion{v1.4}
\def \filedate{2002/02/12}
\def \docdate{\filedate}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ucl_exam}[\filedate\space\fileversion\space UCL Exam Paper class]
\PassOptionsToClass{a4paper,12pt,twoside,onecolumn}{article}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions
\LoadClass{article}
\RequirePackage{times}
\RequirePackage{ucl_a4}
\RequirePackage{ifthen}
\RequirePackage{color} 
\renewcommand{\baselinestretch}{1.5}
\setlength \textheight{24cm}
\setlength \textwidth{16cm}
\raggedbottom
\pagenumbering{arabic}%  Implies \setcounter{page}{1}
\newsavebox{\ctitle}
\newsavebox{\cnumber}
\newsavebox{\cyear}
\newcommand{\coursetitle}[1]{\sbox{\ctitle}{#1}}
\newcommand{\coursenumber}[1]{\sbox{\cnumber}{#1}}
\newcommand{\courseyear}[1]{\sbox{\cyear}{#1}}
\newif \ifcalculatorsnotallowed
\calculatorsnotallowedtrue
\newenvironment{rubric}%
    {\noindent\usebox{\ctitle}, \usebox{\cnumber}, \usebox{\cyear}\\}
    {\\Marks for each part of each question are indicated in square brackets\\%
     Calculators are \ifcalculatorsnotallowed NOT \fi permitted}
\newcommand{\romanmediumupright}{\rmfamily\mdseries\upshape}
\let \@enddocument = \enddocument
\def \enddocument{%
    \vfil%
    %\begin{flushright}%
    %    \romanmediumupright END OF PAPER%
    %\end{flushright}%
    \vfil%
    \romanmediumupright\usebox{\cnumber}\hfill\arabic{page}\hfill\hspace{4em}%
    \thispagestyle{examlast}%
    \@enddocument%
}
\newcommand{\testpagebreak}[1]{%
    \vfil%
    \penalty #1%
    \vfilneg%
}
\newcommand{\questionpenalty}{-350}
\newcommand{\subquestionpenalty}{-200}
\newcommand{\subsubquestionpenalty}{-50}
\newcounter{question}
\newcounter{subquestion}[question]
\renewcommand{\thesubquestion}{\alph{subquestion}}
\newcounter{subsubquestion}[subquestion]
\renewcommand{\thesubsubquestion}{\roman{subsubquestion}}
\let \@headthequestion = \relax
\let \@tailthequestion = \relax
\newenvironment{question}{%
    \refstepcounter{question}%
    \xdef \@tailthequestion{\thequestion}%
    \begin{list}{}{}%
        \item[\thequestion.]%
}{%
    \end{list}%
    \global \let \@tailthequestion = \relax%
    \testpagebreak{\questionpenalty}%
}
\newenvironment{subquestion}{%
    \stepcounter{subquestion}%
    \edef \@currentlabel{\thequestion.\thesubquestion}
    \begin{list}{}{}%
        \item[\thesubquestion.]%
}{%
    \end{list}
    \testpagebreak{\subquestionpenalty}%
}
\newenvironment{subsubquestion}{%
    \stepcounter{subsubquestion}%
    \edef \@currentlabel{\thequestion.\thesubquestion.\thesubsubquestion}
    \begin{list}{}{}%
        \item[\thesubsubquestion.]%
}{%
    \end{list}%
    \testpagebreak{\subquestionpenalty}%
}
\newcommand \further[1]{\csname further#1\endcsname}%
\newcommand \furtherquestion{\end{question}\begin{question}}%
\newcommand \furthersubquestion{\end{subquestion}\begin{subquestion}}%
\newcommand \furthersubsubquestion{\end{subsubquestion}\begin{subsubquestion}}%
\renewcommand \marks[1]{%
    \vspace*{-12pt}%
    \begin{flushright}%
        \romanmediumupright%
        [#1 marks]%
    \end{flushright}%
}%
\newcommand \answermarks[1]{%
    \vspace*{-12pt}%
    \begin{flushright}%
        \romanmediumupright%
        {(#1 marks)~~~~~~~~}%
    \end{flushright}%
}%

%\newcommand{\comment}[1]{\noindent{\bfseries Comment:}#1}

\newif \ifanswersrequired
\answersrequiredfalse
\newcommand \@@header{\ifanswersrequired%
         \setlength{\unitlength}{\textheight}
         \begin{picture}(0,0)(0,1)%
            \includegraphics{answers.pdf}%
         \end{picture}%
         \fi%
         \romanmediumupright \hfill \hspace{1em} \hfill}

\newcommand \@@evenfoot{\romanmediumupright \usebox{\cnumber} \hss%
\arabic{page} \hss CONTINUED}
\newcommand \@@oddfoot{\romanmediumupright \usebox{\cnumber} \hss%
\arabic{page} \hss TURN OVER}
\newcommand \docontinuation{%
  \ifanswersrequired%
  \else%
    \gdef \@texttop{%
        \if \@headthequestion \relax%
            \relax%
        \else%
            \begin{flushleft}%
                \romanmediumupright%
                [Question \@headthequestion\ continued.]%
            \end{flushleft}%
            \global \let \@headthequestion = \relax%
        \fi%
    }%
    \gdef \@textbottom{%
        \if \@tailthequestion \relax%
            \raggedbottom%
        \else%
            \ifodd \value{page}%
                \begin{flushright}%
                    \romanmediumupright%
                    [Question \@tailthequestion\ continued over page.]%
                \end{flushright}%
            \else%
                \begin{flushright}%
                    \romanmediumupright%
                    [Question \@tailthequestion\ continued on next page]%
                \end{flushright}%
            \fi%
            \raggedbottom%
            \global \let \@headthequestion = \@tailthequestion%
        \fi%
    }%
    \fi%
}
\def \ps@exam{%
    \let \@mkboth \@gobbletwo%
    \def \@oddhead{\@@header}%
    \def \@oddfoot{\@@oddfoot}%
    \def \@evenhead{\@@header}%
    \def \@evenfoot{\@@evenfoot}%
}
\def \ps@examlast{%
    \let \@mkboth \@gobbletwo%
    \def \@oddhead{\@@header}%
    \def \@oddfoot{}%
    \def \@evenhead{\@@header}%
    \def \@evenfoot{}%
}
\pagestyle{exam}
\newwrite \@answerfile
\begingroup
    \catcode`|=0%
    \catcode`[= 1%
    \catcode`]=2%
    \catcode`\{=12%
    \catcode`\}=12%
    \catcode`\\=12%
    |global |long |def |@answer#1\end{answer}[%
        |ifanswersrequired%
            |immediate |openout |@answerfile = |jobname.ans%
            |immediate |write |@answerfile[#1]%
            |immediate |closeout |@answerfile%
        |fi
        |end[answer]%
    ]%
|endgroup
\newenvironment{answer}{%
    \begingroup%
        \def \par{^^J}%
        \let \do = \@makeother%
        \dospecials%
        \obeyspaces%
        \obeylines%
        \@answer%
}{%
    \endgroup%
    \ifanswersrequired%
        \begingroup%
            \par%
            \sffamily%
            \mdseries%
            \upshape%
            \def \baselinestretch{1}%
            \footnotesize
            \makeatletter%
            \color{magenta}%
            \input \jobname.ans %%%% --- Crucial space!!!!
            \color{black}%
            \makeatother%
            \par%
        \endgroup%
    \fi%
}
\endinput
%%
%% End of file `ucl_exam.cls'.
