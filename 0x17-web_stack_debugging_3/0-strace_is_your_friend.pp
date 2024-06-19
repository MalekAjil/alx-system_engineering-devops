#Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
class apache_config {
  file_line { 'apache_server_name':
    ensure => present,
    path   => '/etc/apache2/apache2.conf',
    line   => 'ServerName 100.25.46.143',
    match  => '^#?ServerName',
  }
}

include apache_config
