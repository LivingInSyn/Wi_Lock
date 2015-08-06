Param([switch]$debug, $value = 120)

Function Get-RegistryValue([ref]$in)
{
	Write-Debug $MyInvocation.MyCommand.name
	$in.value = (Get-ItemProperty -path $path -name $name).$name
} #end Get-RegistryValue

Function Set-RegistryValue($value)
{
	Write-Debug $MyInvocation.MyCommand.name
	Set-ItemProperty -Path $path -name $name -value $value
} #end Get-RegistryValue

Function Write-Feedback($in)
{
	Write-Debug $MyInvocation.MyCommand.name
	"The $name is set to $($in)"
} #end Write-Feedback

# *** Entry Point ***
if($debug) { $DebugPreference = "continue" }
$path = 'HKCU:\Control Panel\Desktop'
$name = 'ScreenSaveTimeOut'
$in = $null

Get-RegistryValue([ref]$in)
Write-Feedback($in)
Set-RegistryValue($value)
Get-RegistryValue([ref]$in)
Write-Feedback($in)