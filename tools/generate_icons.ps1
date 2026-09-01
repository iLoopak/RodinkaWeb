Add-Type -AssemblyName System.Drawing

function New-RodinkaIcon {
  param(
    [Parameter(Mandatory = $true)][int]$Size,
    [Parameter(Mandatory = $true)][string]$Destination
  )

  $bitmap = [System.Drawing.Bitmap]::new($Size, $Size)
  $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
  $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $graphics.Clear([System.Drawing.ColorTranslator]::FromHtml('#f7f2e8'))
  $scale = $Size / 235.0

  $shapes = @(
    @{ X = 34; Y = 87; Width = 48; Height = 92; Color = '#e9785e'; Rotation = -12; CenterX = 58; CenterY = 133 },
    @{ X = 92; Y = 44; Width = 52; Height = 134; Color = '#f2c85b'; Rotation = 0; CenterX = 118; CenterY = 111 },
    @{ X = 154; Y = 73; Width = 48; Height = 106; Color = '#8bc6ad'; Rotation = 12; CenterX = 178; CenterY = 126 }
  )

  foreach ($shape in $shapes) {
    $state = $graphics.Save()
    $graphics.TranslateTransform($shape.CenterX * $scale, $shape.CenterY * $scale)
    $graphics.RotateTransform($shape.Rotation)
    $graphics.TranslateTransform(-$shape.CenterX * $scale, -$shape.CenterY * $scale)
    $brush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($shape.Color))
    $graphics.FillEllipse($brush, $shape.X * $scale, $shape.Y * $scale, $shape.Width * $scale, $shape.Height * $scale)
    $brush.Dispose()
    $graphics.Restore($state)
  }

  $bitmap.Save($Destination, [System.Drawing.Imaging.ImageFormat]::Png)
  $graphics.Dispose()
  $bitmap.Dispose()
}

New-RodinkaIcon -Size 96 -Destination (Join-Path $PSScriptRoot '..\favicon-96.png')
New-RodinkaIcon -Size 180 -Destination (Join-Path $PSScriptRoot '..\apple-touch-icon.png')
