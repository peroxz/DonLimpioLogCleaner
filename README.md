# DonLimpioLogCleaner
Search keywords from a list in a big log file and print the matched line. It supports to invert the sense of matching.

The output prints to STDOUT. It's like a supergrep command.

You can grep GB logs in minutes. For example: 8000 keywords to 35 GB logs in 85 minutes.

  ## Help
  
Check the options:
  
    $ ./donLimpioCleaner.py --help
    usage: donLimpioCleaner.py [-h] -i FILE -f FILE [-v]

    optional arguments:
      -h, --help            show this help message and exit
      -i FILE, --input FILE
                            Obtain patterns from FILE, one per line
      -f FILE, --file FILE  Obtain log file to process
      -v, --invert-match    Invert the sense of matching, to select non-matching
                            lines.

Run DonLimpioLogCleaner to match:

    $ ./donLimpioCleaner.py -i ip_list.txt -f firewall.log

Run DonLimpioLogCleaner to inverted match:

    $ ./donLimpioCleaner.py -i ip_list.txt -f firewall.log -v

  ## Install
  
       pip3 install flashtext
  
  ## Software
 - Python 3
 - flashtext
 
  ## References
  https://dev.to/vi3k6i5/regex-was-taking-5-days-to-run-so-i-built-a-tool-that-did-it-in-15-minutes-c98
