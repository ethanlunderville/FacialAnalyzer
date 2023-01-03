dir="$FACEPROJECTDIR/output/image-output"

declare -a files=$( ls $dir )

for file in $dir/*; do
  files+=("$file")
  echo "<img src=\"$file\">"
done

