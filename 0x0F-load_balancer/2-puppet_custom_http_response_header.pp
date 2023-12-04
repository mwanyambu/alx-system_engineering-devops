#!/usr/bin/env bash
# script uses puppet to create cutom hhtp header

exec {'update':
   command => '/usr/bin/apt-get update',
}
-> package {'nginx':
    ensure => 'present',
}
-> file_line { 'http_header':
    path => '/etc/nginx/nginx.conf',
    match => 'http {',
    line  => "http {\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
    command => '/usr/sbin/service nginx restart',
}
