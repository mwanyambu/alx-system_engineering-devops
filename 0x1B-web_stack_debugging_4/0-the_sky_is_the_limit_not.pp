#configure web server to work under pressure
exec { '/usr/bin/env sed -i s/15/1000/ etc/default/nginx':
  command => '/usr/bin/env sed -i s/15/1000/ etc/default/nginx',
}
exec { '/usr/bin/env service nginx restart':
  command => '/usr/bin/env service nginx restart',
  require => Exec['/usr/bin/env sed -i s/15/1000/ etc/default/nginx'],
}
