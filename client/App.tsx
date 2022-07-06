import { StyleSheet, Text, View } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';

import StartScreen from './screens/StartScreen';

export default function App() {
	return (
		<SafeAreaProvider>
			<View style={styles.container}>
				<StartScreen />
			</View>
		</SafeAreaProvider>
	);
}

const styles = StyleSheet.create({
	container: {
		flex: 1,
		// backgroundColor: '#fff',
		// alignItems: "center",
		// justifyContent: "center",
	},
});