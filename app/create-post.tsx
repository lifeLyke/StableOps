import * as Clipboard from 'expo-clipboard';
import { Stack, useRouter } from 'expo-router';
import { useState } from 'react';
import { Alert, Keyboard, ScrollView, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

export default function CreatePostScreen() {
  const router = useRouter();
  const [details, setDetails] = useState('');
  const [platform, setPlatform] = useState('both');
  const [generatedPost, setGeneratedPost] = useState('');

  return (
    <>
      <Stack.Screen options={{ headerShown: false }} />
      <ScrollView style={styles.container}>
        <TouchableOpacity onPress={() => router.back()}>
          <Text style={styles.backButton}>← Back</Text>
        </TouchableOpacity>

        <Text style={styles.title}>Create Social Post</Text>
        <Text style={styles.subtitle}>This is where Emily will create posts</Text>

        <Text style={styles.label}>What's this post about?</Text>
        <TextInput
          style={styles.input}
          placeholder="E.g., Fall festival on Nov 5th, tickets $20..."
          value={details}
          onChangeText={setDetails}
          multiline
        />

        <Text style={styles.label}>Platform</Text>
        <View style={styles.platformContainer}>
          <TouchableOpacity
            style={[styles.platformButton, platform === 'instagram' && styles.platformButtonActive]}
            onPress={() => setPlatform('instagram')}
          >
            <Text style={[styles.platformButtonText, platform === 'instagram' && styles.platformButtonTextActive]}>Instagram</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.platformButton, platform === 'facebook' && styles.platformButtonActive]}
            onPress={() => setPlatform('facebook')}
          >
            <Text style={[styles.platformButtonText, platform === 'facebook' && styles.platformButtonTextActive]}>Facebook</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.platformButton, platform === 'both' && styles.platformButtonActive]}
            onPress={() => setPlatform('both')}
          >
            <Text style={[styles.platformButtonText, platform === 'both' && styles.platformButtonTextActive]}>Both</Text>
          </TouchableOpacity>
        </View>

        <TouchableOpacity 
          style={styles.generateButton}
           onPress={() => {
             Keyboard.dismiss();
  
             let post = '';
             if (platform === 'instagram' || platform === 'both') {
              post += `🐴 ${details}\n\nJoin us and be part of something special! ❤️\n\n#therapeuticriding #horses #community #nonprofit\n\n`;
             }
             if (platform === 'facebook' || platform === 'both') {
              post += `We're excited to share some news from our farm!\n\n${details}\n\nWe'd love to see you there. Tag a friend who would enjoy this! 🐎`;
             }
  
             setGeneratedPost(post);
           }}
        >
          <Text style={styles.generateButtonText}>Generate Post ✨</Text>
        </TouchableOpacity>

        {generatedPost !== '' && (
          <View style={styles.resultContainer}>
            <Text style={styles.resultLabel}>Generated Post:</Text>
            <Text style={styles.resultText}>{generatedPost}</Text>
            <TouchableOpacity 
             style={styles.copyButton}
             onPress={() => {
              Clipboard.setStringAsync(generatedPost);
              Alert.alert('Copied!', 'Post copied to clipboard');
             }}
           >
             <Text style={styles.copyButtonText}>Copy to Clipboard</Text>
           </TouchableOpacity>
          </View>
        )}
      </ScrollView>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    paddingTop: 60,
    paddingBottom: 40,
    backgroundColor: '#ffffff',
  },
  backButton: {
    fontSize: 16,
    color: '#4a90d9',
    marginBottom: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#666666',
  },
  label: {
    fontSize: 16,
    fontWeight: '600',
    marginTop: 24,
    marginBottom: 8,
  },
  input: {
    borderWidth: 1,
    borderColor: '#cccccc',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
    minHeight: 100,
    textAlignVertical: 'top',
  },
  platformContainer: {
    flexDirection: 'row',
    gap: 8,
  },
  platformButton: {
    flex: 1,
    padding: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#cccccc',
    alignItems: 'center',
  },
  platformButtonActive: {
    backgroundColor: '#4a90d9',
    borderColor: '#4a90d9',
  },
  platformButtonText: {
    fontSize: 14,
    color: '#666666',
  },
  platformButtonTextActive: {
    color: '#ffffff',
    fontWeight: '600',
  },
  generateButton: {
    backgroundColor: '#4a90d9',
    padding: 16,
    borderRadius: 8,
    marginTop: 32,
    alignItems: 'center',
  },
  generateButtonText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: '600',
  },
  resultContainer: {
    marginTop: 24,
    padding: 16,
    backgroundColor: '#f5f5f5',
    borderRadius: 8,
  },
  resultLabel: {
    fontSize: 14,
    fontWeight: '600',
    marginBottom: 8,
    color: '#666666',
  },
  resultText: {
    fontSize: 16,
    lineHeight: 24,
  },

  copyButton: {
  marginTop: 16,
  padding: 12,
  backgroundColor: '#28a745',
  borderRadius: 8,
  alignItems: 'center',
  },
  copyButtonText: {
  color: '#ffffff',
  fontSize: 16,
  fontWeight: '600',
  },
});