#Using strace, find out why Apache is returning a 500 error.
#Once you find the issue, fix it and then automate it using Puppet
#(instead of using Bash as you were previously doing).
file_line { 'correct_config_setting':
  ensure => present,
  path   => '/path/to/config/file',
  line   => 'Correct configuration line',
  match  => '^Incorrect configuration line',
}
