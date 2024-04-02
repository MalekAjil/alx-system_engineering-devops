package { 'nginx':
  ensure => installed,
}
file { '/etc/nginx/conf.d/custom_headers.conf':
  content => "server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://localhost:8080;
        add_header X-Served-By $hostname;
    }
}\n",
  notify  => Service['nginx'],
}
exec { 'nginx-test':
  command => 'nginx -t',
  path    => '/usr/sbin',
  require => File['/etc/nginx/conf.d/custom_headers.conf'],
}
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_headers.conf'],
}
