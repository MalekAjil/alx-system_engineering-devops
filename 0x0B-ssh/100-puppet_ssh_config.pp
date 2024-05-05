#!/usr/bin/env bash
class ssh_config {
  file { '/etc/ssh/ssh_config':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('ssh/ssh_config.erb'),
  }
}
