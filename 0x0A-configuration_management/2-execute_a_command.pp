# a manifest that kills a process named killmenow.
exec { 'kill-killmenow-process':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
