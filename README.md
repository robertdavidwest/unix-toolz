# unix-toolz
Tools to be used on the Unix command line - for previewing data prettily and such

# instuctions for use in unix

* after cloning this repo at the path to the ~/.bashrc file. e.g:
        
        export PATH="/home/rwest/github/unix-toolz:$PATH"

* then do: `$chmod +x filename` on all commands that will be used form the library: 

        $ chmod +x preview-s3-csv
        $ chmod +x preview-s3-logs

* then run `source ~/.bashrc` to update the terminal
* now your system will know the command `preview-s3-logs`
* for example. given the currenr config setup. The follow command will preview the loggged traceback for the lds transform process:

        $ preview-s3-logs transform-lds-reruns

and thats it!

This project will updated and become more general as it grows
